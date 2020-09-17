#!/usr/bin/env python3
import redis

redis_host = "localhost"
redis_port = 6379
redis_password = ""

def cloudacademy_redis():
    try:
        r = redis.Redis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)

        r.set("course1", "Introduction to Redis")
        r.set("course2", "Introduction to Python")
        r.set("course3", "Introduction to Java")
        r.set("course4", "Introduction to C#")

        course1 = r.get("course1")
        course2 = r.get("course2")
        course3 = r.get("course3")
        course4 = r.get("course4")

        print(course1)
        print(course2)
        print(course3)
        print(course4)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    cloudacademy_redis()