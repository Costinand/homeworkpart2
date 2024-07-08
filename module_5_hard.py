import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return f"User(nickname='{self.nickname}', age={self.age})"

    def check_password(self, password):
        return self.password == hash(password)


class Video:
    def __init__(self, title, duration, time_now, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __str__(self):
        return f"Video(title'{self.title}', duration{self.duration} seconds"

    def is_adult(self):
        return self.adult_mode


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, login, password):
        for user in self.users:
            if user.nickname == login and user.check_password(password):
                self.current_user = user
                return
            print("Неверное имя или пароль")

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return

        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
        print(f"Пользователь {nickname} успешно зарегестрирован и вошел в аккаунт")

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            if video.title not in [vN.title for vN in self.videos]:
                self.videos.append(video)
        else:
            print(f"Видео с названием '{video.title}' уже существует")

    def get_videos(self, search_word):
        found_videos = []
        for video in self.videos:
            if search_word.lower() in video.title.lower():
                found_videos.append(video.title)
        return found_videos


    def watch_video(self, video_title):

        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        found_video = None
        for video in self.videos:
            if video.title.lower() == video_title.lower():
                found_video = video
                break

        if not found_video:
            print(f"Видео '{video_title}' не найдено")
            return

        if found_video.is_adult() and self.current_user.age < 18:
            print(("Вам нет 18 лет, пожалуйста покиньте страницу"))
            return
        print(f"Начало воспроизведения видео '{found_video.title}'")
        for second in range(1, found_video.duration + 1):
            print(second, end=' ')
            time.sleep(1)

        print('\nконец видео')

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200, 3)
v2 = Video('Для чего девушкам парень программист?', 10, 4, adult_mode=True)

ur.add(v1, v2)

print(ur.get_videos('лучший'))
print(ur.get_videos('прог'))

ur.watch_video('Для чего девушкам парень программист?')
ur.register('kuzya_zloy', 'bedaogor4enie', 15)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('free_artist', 'vo1jv17dfUn', 32)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('kuzya_zloy', 'nafanyaTiGde', 45)
print(ur.current_user)

