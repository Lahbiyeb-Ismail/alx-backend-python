#!/usr/bin/env python3
access_nested_map = __import__("utils").access_nested_map
get_json = __import__("utils").get_json

# nested_map = {"a": 1}
# path = ("a",)

# print(access_nested_map(nested_map, path))

# nested_map = {"a": {"b": 2}}
# path = ("a",)

# print(access_nested_map(nested_map, path))

# nested_map = {}
# path = ("a",)

# print(access_nested_map(nested_map, path))

# nested_map = {"a": 1}
# path = ("a", "b")

# print(access_nested_map(nested_map, path))

test_url="http://example.com", test_payload={"payload": True}

print(get_json())

test_url="http://holberton.io", test_payload={"payload": False}
