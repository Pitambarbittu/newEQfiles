terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
#   backend "s3" {
#     bucket = "pitambar-s3-bucket"
#     key    = "pitambar.tfstate"
#     region = "us-east-1"
#   }
}


provider "aws" {
  region = var.region
}