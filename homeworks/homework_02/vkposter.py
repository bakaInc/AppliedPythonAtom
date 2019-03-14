#!/usr/bin/env python
# coding: utf-8


from homeworks.homework_02.heap import MaxHeap
from homeworks.homework_02.fastmerger import FastSortedListMerger


class VKPoster:

    def __init__(self):
        self.autor_post = {}
        self.post_reader = {}
        self.user_follow = {}

    def user_posted_post(self, user_id: int, post_id: int):
        if user_id in self.autor_post.keys():
            self.autor_post[user_id].append(post_id)
        else:
            self.autor_post[user_id] = [post_id]

    def user_read_post(self, user_id: int, post_id: int):
        if post_id in self.post_reader.keys():
            self.post_reader[post_id].add(user_id)
        else:
            self.post_reader[post_id] = set([user_id])

    def user_follow_for(self, follower_user_id: int, followee_user_id: int):
        if follower_user_id in self.user_follow.keys():
            self.user_follow[follower_user_id].append(followee_user_id)
        else:
            self.user_follow[follower_user_id] = [followee_user_id]

    def get_recent_posts(self, user_id: int, k: int) -> list:
        out = []
        for user in self.user_follow[user_id]:
            if user in self.autor_post.keys():
                for i in self.autor_post[user]:
                    out.append(i)
        return sorted(out, reverse=True)[:k]

    def get_most_popular_posts(self, k: int) -> list:
        out_num = []
        out = []
        N = 0
        for post in self.post_reader.keys():
            out_num.append(len(self.post_reader[post]))
        out_num_s = sorted(out_num, reverse=True)
        i = -1
        while i < len(out_num):
            i += 1
            out_1 = []
            for p in self.post_reader.keys():
                if out_num_s[i] == len(self.post_reader[p]):
                    out_1.append(p)
                    N += 1
            out_2 = sorted(out_1, reverse=True)
            out = out + out_2
            if N >= k:
                i = len(out_num)
        return out[:k]
