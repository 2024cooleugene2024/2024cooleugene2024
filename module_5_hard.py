import hashlib
from time import sleep


class User:
    """
    Класс User представляет пользователя с никнеймом, паролем и возрастом.

    Параметры:
    ----------
    nickname : str
        Никнейм пользователя.
    password : str
        Исходный пароль пользователя, который будет захеширован.
    age : int
        Возраст пользователя.
    """

    def __init__(self, nickname: str, password: str, age: int):
        """
        Инициализирует объект пользователя.

        Параметры:
        ----------
        nickname : str
            Никнейм пользователя.
        password : str
            Пароль пользователя.
        age : int
            Возраст пользователя.
        """
        self.nickname = nickname
        self.password = User.hash_password(password)
        self.age = age

    @staticmethod
    def hash_password(password: str) -> str:
        """
        Захешировать пароль с использованием SHA-256.

        Параметры:
        ----------
        password : str
            Пароль для хеширования.

        Возвращает:
        ----------
        str
            Захешированный пароль.
        """
        return hashlib.sha256(password.encode()).hexdigest()

    def __eq__(self, other) -> bool:
        """
        Проверяет равенство двух пользователей.

        Параметры:
        ----------
        other : User
            Другой пользователь для сравнения.

        Возвращает:
        ----------
        bool
            True, если пользователи равны, иначе False.
        """
        if not isinstance(other, User):
            return NotImplemented
        return self.nickname == other.nickname and self.password == other.password and self.age == other.age

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта пользователя.

        Возвращает:
        ----------
        str
            Строковое представление объекта.
        """
        return f'User({self.nickname!r}, {self.age})'


class Video:
    """
    Класс Video представляет видео с названием, длительностью и опциональной настройкой для взрослых.

    Параметры:
    ----------
    title : str
        Название видео.
    duration : int
        Длительность видео в секундах.
    adult_mode : bool, по умолчанию False
        Если установлено в True, видео предназначено только для взрослых.
    """

    def __init__(self, title: str, duration: int, adult_mode: bool = False):
        """
        Инициализирует объект видео.

        Параметры:
        ----------
        title : str
            Название видео.
        duration : int
            Длительность видео в секундах.
        adult_mode : bool, по умолчанию False
            Если установлено в True, видео предназначено только для взрослых.
        """
        self.title = title
        self.duration = duration
        self.current_time = 0
        self.adult_mode = adult_mode

    def __eq__(self, other) -> bool:
        """
        Проверяет равенство двух видео на основе названия.

        Параметры:
        ----------
        other : Video
            Другое видео для сравнения.

        Возвращает:
        ----------
        bool
            True, если видео равны, иначе False.
        """
        if not isinstance(other, Video):
            return NotImplemented
        return self.title == other.title

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта видео.

        Возвращает:
        ----------
        str
            Строковое представление объекта.
        """
        return f'Video({self.title!r}, {self.duration}, {self.adult_mode})'


class UrTube:
    """
    Класс UrTube представляет платформу для обмена видео.

    Атрибуты:
    --------
    users : dict
        Словарь с пользователями, где ключ — никнейм, значение — объект User.
    videos : list
        Список всех видео на платформе.
    current_user : User or None
        Текущий авторизованный пользователь.
    """

    def __init__(self):
        """
        Инициализирует пустую платформу UrTube.
        """
        self.users = {}
        self.videos = []
        self.current_user = None

    def log_in(self, nickname: str, password: str) -> None:
        """
        Вход пользователя в систему.

        Параметры:
        ----------
        nickname : str
            Никнейм пользователя.
        password : str
            Пароль пользователя.
        """
        hashed_password = User.hash_password(password)
        user = self.users.get(nickname)
        if user and user.password == hashed_password:
            self.current_user = user
        else:
            print("Неверные учетные данные")

    def register(self, nickname: str, password: str, age: int) -> None:
        """
        Регистрация нового пользователя.

        Параметры:
        ----------
        nickname : str
            Никнейм пользователя.
        password : str
            Пароль пользователя.
        age : int
            Возраст пользователя.
        """
        if nickname in self.users:
            print(f"Пользователь {nickname} уже существует")
        else:
            new_user = User(nickname, password, age)
            self.users[nickname] = new_user
            self.current_user = new_user

    def log_out(self) -> None:
        """
        Выход пользователя из системы.
        """
        self.current_user = None

    def add(self, *videos) -> None:
        """
        Добавление видео на платформу.

        Параметры:
        ----------
        videos : Video
            Одно или несколько видео для добавления.
        """
        for video in videos:
            if not isinstance(video, Video):
                print(f"Объект {video} не является видео")
                continue
            if video not in self.videos:
                self.videos.append(video)

    def get_videos(self, keyword: str) -> list:
        """
        Поиск видео по ключевому слову.

        Параметры:
        ----------
        keyword : str
            Ключевое слово для поиска.

        Возвращает:
        ----------
        list
            Список видео, которые соответствуют ключевому слову.
        """
        keyword = keyword.lower()
        return [video for video in self.videos if keyword in video.title.lower()]

    def watch_video(self, title: str) -> None:
        """
        Просмотр видео.

        Параметры:
        ----------
        title : str
            Название видео для просмотра.
        """
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        video_to_watch = next((video for video in self.videos if video.title == title), None)
        if video_to_watch is None:
            print("Видео не найдено")
            return

        if video_to_watch.adult_mode and self.current_user.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return

        for second in range(video_to_watch.current_time, video_to_watch.duration):
            print(second + 1, end=" ", flush=True)
            sleep(1)
        print("Конец видео")
        video_to_watch.current_time = 0


# Пример использования
if __name__ == "__main__":
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 10)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    ur.add(v1, v2)
    print([v.title for v in ur.get_videos('лучший')])
    print([v.title for v in ur.get_videos('ПРОГ')])

    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    ur.log_in('vasya_pupkin', 'F8098FM8fjm9jmi')
    print(ur.current_user)

    ur.watch_video('Лучший язык программирования 2024 года!')