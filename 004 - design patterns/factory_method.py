from abc import ABCMeta, abstractmethod

class Session(metaclass=ABCMeta):
    @abstractmethod
    def description(self):
        pass

class ProfileSession(Session):
    def description(self):
        print('Profile session')

class AlbumSession(Session):
    def description(self):
        print('Album session')

class PostSession(Session):
    def description(self):
        print('Post session')


class Profile(metaclass=ABCMeta):
    def __init__(self):
        self.sessions = []
        self.make_profile()

    @abstractmethod
    def make_profile(self):
        pass

    def get_sessions(self):
        return self.sessions

    def add_sessions(self, session):
        self.sessions.append(session)


class Facebook(Profile):
    def make_profile(self):
        self.add_sessions(ProfileSession())
        self.add_sessions(PostSession())

class Instagram(Profile):
    def make_profile(self):
        self.add_sessions(ProfileSession())
        self.add_sessions(AlbumSession())


if __name__ == '__main__':
    profile_type = 'Instagram'
    profile = eval(profile_type)()
    print(profile.get_sessions())

    profile_type = 'Facebook'
    profile = eval(profile_type)()
    print(profile.get_sessions())

    # Eval must be secured!
    # eval('print("OOPS")')