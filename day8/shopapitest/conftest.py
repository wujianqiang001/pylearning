# replace this:
# marker = item.get_marker("log_level")
# if marker:
#     level = marker.args[0]
#
# # by this:
# marker = item.get_closest_marker("log_level")
# if marker:
#     level = marker.args[0]