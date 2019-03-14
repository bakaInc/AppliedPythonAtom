#!/usr/bin/env python
# coding: utf-8


from homeworks.homework_02.heap import MaxHeap
from homeworks.homework_02.fastmerger import FastSortedListMerger


class VKPoster:

    def __init__(self):
        raise NotImplementedError

    def user_posted_post(self, user_id: int, post_id: int):
        pass

    def user_read_post(self, user_id: int, post_id: int):
        pass

    def user_follow_for(self, follower_user_id: int, followee_user_id: int):
        pass

    def get_recent_posts(self, user_id: int, k: int) -> list:
        pass
