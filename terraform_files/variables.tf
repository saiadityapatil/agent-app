variable "resource_group_name" {
  default = "agent-demo-rg"
}

variable "location" {
  default = "Central India"
}

variable "app_name" {
  default = "agent-fastapi-demo-1234"
}

variable "sql_server_name" {
  default = "agent-sql-server-1234"
}

variable "database_name" {
  default = "agentdb"
}

variable "sql_admin" {
  description = "SQL admin username"
}

variable "sql_password" {
  description = "SQL admin password"
  sensitive   = true
}
