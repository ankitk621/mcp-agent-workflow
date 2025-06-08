resource "catchpoint_transaction_test" "product_price_monitor" {
  provider     = catchpoint
  product_id   = var.product_id
  division_id  = var.division_id
  test_name    = var.test_name
  script       = var.test_script
  status       = "active"

  schedule_settings {
    frequency             = "15 minutes"
    node_distribution     = "random"
    nodes_in_rotation     = 2
    consecutive_failures  = 1
  }
}
