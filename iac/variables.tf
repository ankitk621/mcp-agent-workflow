variable "test_name" {
  type        = string
  description = "The name of the synthetic test."
}
variable "product_id" {
  type        = number
  description = "The Catchpoint Product ID."
}
variable "division_id" {
  type        = number
  description = "The Catchpoint Division ID."
}
variable "test_script" {
  type        = string
  description = "The transaction script to execute."
  sensitive   = true
}
