from HW1.classes.connection import Connection
from HW1.tests.test1_login import Test1_login
from HW1.tests.test2_add_2prod import Test2_add_2prod
from HW1.tests.test3_remove import Test3_remove
from HW1.tests.test4_cancel import Test4_cancel
from HW1.tests.test5_manu import Test5_manu

con=Connection("chromium",100)
page = con.new_page()
test1=Test1_login(page)
test1.run_test1_login()
# Test 2 add 2 product and checkout
test2=Test2_add_2prod(page)
test2.run_test2_ad_2prod()
# Test 3 remove 2 product
test3=Test3_remove(page)
test3.run_test3_remove()
# Test 4 cancel order
test4=Test4_cancel(page)
test4.run_test4_cancel()
# Test 5 manu actions
test5=Test5_manu(page)
test5.run_test5_manu()
