
test_name    = "E-commerce Price Verification for Leather Jacket"
product_id   = 15330
division_id  = 1000
test_script  = "// Step 1: Login\nopen(\"https://www.saucedemo.com\");\ntype(\"id=user-name\", \"standard_user\");\ntype(\"id=password\", \"secret_sauce\");\nclick(\"id=login-button\");\n// Step 2: Add item and verify our dynamic text\nclick(\"id=add-to-cart-sauce-labs-backpack\");\nverifyTextPresent(\"$122.50\");"
