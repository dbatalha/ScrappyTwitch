import schedule
import logging
from termcolor import colored

from scrappy_bot.core.data.stream_status import StreamStatus
from scrappy_bot.core.properties_reader import PropertiesReader
from scrappy_bot.core.twitch_requests import TwitchRequests
from scrappy_bot.session.login import Login
from scrappy_bot.session.stream import Stream
from scrappy_bot.session.user import User
from scrappy_bot.session.watcher import Watcher
from scrappy_bot.core.gateways.users_gateway import UsersGateway
from scrappy_bot.core.gateways.watch_gateway import WatchGateway
from scrappy_bot.core.gateways.streams_gateway import StreamsGateway

login_object = Login()
streams_status = []
properties = PropertiesReader()
logging.basicConfig(filename=properties.get_file_location(), level=logging.DEBUG)
logger = logging.getLogger(properties.get_scrappy_bot())


def do_login():
    global login_object
    request_call = TwitchRequests(login_object, None, None)
    request_call.login()


def do_add_streamer(watch_flow, streamer):
    watcher_object = Watcher()
    watcher_object.set_name(streamer)
    watch_flow.add_watcher(watcher_object)


def status_change_detector(actual_status):
    for stream in streams_status:
        for actual in actual_status:
            if stream.get_stream() == actual.get_stream():
                logger.info("Stream: {} Status: {}".format(actual.get_stream(), actual.get_status()))
                if stream.get_status() != actual.get_status():
                    logger.debug("Status change detected Stream: {} Status: {}".format(
                        actual.get_stream(), actual.get_status()))
                    print("----> Status changed")


def job():
    global login_object
    global streams_status
    global logger
    user_object = User()
    stream_object = Stream()

    watch_flow = WatchGateway()
    do_add_streamer(watch_flow, "Z3RGtv")
    do_add_streamer(watch_flow, "SheisDani")
    do_add_streamer(watch_flow, "TONIDOROCK")
    do_add_streamer(watch_flow, "itscuegod")
    do_add_streamer(watch_flow, "Ska_zy")
    do_add_streamer(watch_flow, "RavenVonBloodimir")
    do_add_streamer(watch_flow, "PirateSoftware")
    do_add_streamer(watch_flow, "0ficialpi")
    do_add_streamer(watch_flow, "twitchcamponia97")
    do_add_streamer(watch_flow, "WitchcraftCave")
    do_add_streamer(watch_flow, "soniagoncalves")
    streamers = watch_flow.get_all_watchers()

    streams_online = []

    for streamer in streamers:
        request_call = TwitchRequests(login_object, user_object, stream_object)
        request_call.login()

        logger.debug("Get streams for user: {} ".format(streamer))
        request_call.users(streamer)
        request_call.streams(user_object.get_user_id())

        user_flow = UsersGateway()
        user_flow.save_user(user_object)

        streams_gateway = StreamsGateway()
        streams_gateway.create_stream(stream_object)

        if stream_object.get_user_name() is None:
            logger.debug("Stream object is empty, skip stream_object name: {}".format(stream_object.get_user_name()))
            continue

        logger.debug("The stream: {} is Online".format(stream_object.get_user_name()))
        streams_online.append(stream_object.get_user_name())

    actual_status = []
    for stream in watch_flow.get_all_watchers():
        streams_gateway = StreamsGateway()
        is_online = False
        if stream in streams_online:
            logger.debug("The stream : {} was found!".format(stream))
            is_online = True

        stream_status = StreamStatus()
        stream_status.set_stream(stream)
        if not is_online:
            logger.info("The user: {} is Offline".format(stream))
            stream_status.set_status("Offline")
            actual_status.append(stream_status)
            logger.debug("Delete streams for user: {}".format(stream))
            streams_gateway.delete_stream(stream)
        else:
            logger.info("The user: {} is Online".format(stream))
            stream_status.set_status("Online")
            actual_status.append(stream_status)
            logger.debug("Keep the stream for user: {}".format(stream))

    if not streams_status:
        streams_status = actual_status
        return

    status_change_detector(actual_status)
    streams_status = actual_status


def start():
    print("Hello I am scrappy! I am a Twitch bot.")
    print("Alpha v0.1")

    do_login()
    schedule.every(1).minute.do(job)

    print(colored('Running ', 'green'), colored('...', 'blue'),
          colored(" > ", "red"))

    while True:
        schedule.run_pending()
