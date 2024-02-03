import schedule
from termcolor import colored
from scrappy_bot.core.twitch_requests import TwitchRequests
from scrappy_bot.session.login import Login
from scrappy_bot.session.stream import Stream
from scrappy_bot.session.user import User
from scrappy_bot.session.watcher import Watcher
from scrappy_bot.core.flows.users_flow import UsersFlow
from scrappy_bot.core.flows.watch_flow import WatchFlow
from scrappy_bot.core.flows.streams_flow import StreamsFlow

login_object = Login()


def do_login():
    global login_object
    request_call = TwitchRequests(login_object, None, None)
    request_call.login()


def do_add_streamer(watch_flow, streamer):
    watcher_object = Watcher()
    watcher_object.set_name(streamer)
    watch_flow.add_watcher(watcher_object)


def job():
    global login_object
    user_object = User()
    stream_object = Stream()

    watch_flow = WatchFlow()
    do_add_streamer(watch_flow, "Z3RGtv")
    do_add_streamer(watch_flow, "SheisDani")
    do_add_streamer(watch_flow, "TONIDOROCK")
    do_add_streamer(watch_flow, "itscuegod")
    do_add_streamer(watch_flow, "Ska_zy")
    streamers = watch_flow.get_all_watchers()

    for streamer in streamers:
        request_call = TwitchRequests(login_object, user_object, stream_object)
        request_call.login()

        request_call.users(streamer.get("name"))
        request_call.streams(user_object.get_user_id())

        user_flow = UsersFlow()
        user_flow.save_user(user_object)

        streams_flow = StreamsFlow()
        streams_flow.create_stream(stream_object, streamer.get("name"))


def start():
    print("Hello I am scrappy! I am a Twitch bot.")
    print("Alpha v0.1")

    do_login()

    schedule.every(1).minute.do(job)

    print(colored('Running ', 'green'), colored('...', 'blue'),
          colored(" > ", "red"))

    while True:
        schedule.run_pending()
