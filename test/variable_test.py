from hamcrest import assert_that, close_to

from common.exception_handle import ExceptionHandle

handles = ExceptionHandle.get_all_handle()
handles[0].retry_time = 2
print(handles[1].retry_time)

ExceptionHandle.retry_time = 2
print(handles[2].retry_time)


