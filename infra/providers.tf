provider "google" {
  project = var.gcp_project_id
  region  = var.gcp_region
}

terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0.0"
    }
    archive = {
      source  = "hashicorp/archive"
      version = "~> 2.2.0"
    }
  }
  backend "gcs" {
    bucket = "terraform-state-bucket-gcp-practice-project-aman"
    prefix = "cloud-function/xlsx-to-csv-function"
  }
}
