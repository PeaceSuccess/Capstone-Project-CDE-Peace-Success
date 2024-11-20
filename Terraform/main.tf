terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "5.76.0"
    }
  }
}

provider "aws" {
  region= "us-east-1"
}

resource "aws_s3_bucket" "cde_capstone_peace" {
  bucket = "cde-peace-bucket"

  tags = {
    Name        = "PeaceBucket"
  }
}