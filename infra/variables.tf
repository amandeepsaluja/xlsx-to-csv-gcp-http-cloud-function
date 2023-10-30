
variable "gcp_project_id" {
  type        = string
  description = "Google project ID"
  default     = "gcp-practice-project-aman"
}

variable "gcp_region" {
  type        = string
  description = "Google project region"
  default     = "us-central1"
}

variable "name" {
  description = "A user-defined name of the function."
  type        = string
  default     = "xlsx-to-csv-function"
}

variable "description" {
  description = "User-provided description of a function."
  type        = string
  default     = "Cloud function to convert Excel file to CSV via Cloud Function"
}

variable "runtime" {
  description = "The runtime in which to run the function. Required when deploying a new function, optional when updating an existing function."
  type        = string
  default     = "python311"
}

variable "entry_point" {
  description = "The name of the function (as defined in source code) that will be executed. Defaults to the resource name suffix, if not specified. For backward compatibility, if function with given name is not found, then the system will try to use function named \"function\". For Node.js this is name of a function exported by the module specified in source_location."
  type        = string
  default     = "convert_excel_to_csv"
}

variable "max_instance_count" {
  description = "(Optional) The limit on the maximum number of function instances that may coexist at a given time."
  type        = number
  default     = 100
}

variable "available_memory" {
  description = "(Optional) The amount of memory in MB available for a function. Defaults to 256MB."
  type        = string
  default     = "1024M"
}

variable "timeout_seconds" {
  description = "(Optional) The function execution timeout. Execution is considered failed and can be terminated if the function is not completed at the end of the timeout period. Defaults to 60 seconds."
  type        = number
  default     = 420
}

variable "bucket_name" {
  description = "The bucket name where the cloud function code will be stored"
  type        = string
  default     = "cloud-function-bucket-gcp-practice-project-aman"
}


variable "service_account_email" {
  description = "Service account email to be used by cloud function to access other GCP resources passed via Github secrets"
  type        = string
}
