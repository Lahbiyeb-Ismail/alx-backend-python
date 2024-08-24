#!/usr/bin/env python3
access_nested_map = __import__("utils").access_nested_map

nested_map = {"a": 1}
path = ("a",)

print(access_nested_map(nested_map, path))

nested_map = {"a": {"b": 2}}
path = ("a",)

print(access_nested_map(nested_map, path))

nested_map = {"a": {"b": 2}}
path = ("a", "b")

print(access_nested_map(nested_map, path))
