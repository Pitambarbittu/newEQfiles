resource "aws_instance" "terra_instance" {
  ####### count = length(var.t1)
  count = 3
  

  ami                     = "ami-061183ad486d5dd8a"
  instance_type           = "t2.micro"
  tags = {
    Name = var.t1[count.index]
    purpose = "Training"
    Owner = "pitambar.bhadra@cloudeq.com"
  }

  volume_tags = {
    Name = "pitambar"
    purpose = "Training"
    Owner = "pitambar.bhadra@cloudeq.com"
  }
}

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}

provider "aws" {
 region = "ap-south-1"
#  access_key = "ASIAXWDRTCCOKNQTYG7O"
#  secret_key = "UmDadyGxVh64Tc9ao7TJpQGmw7gYGMP7BY6Nv0Kl"
#  shared_config_files       = ["/Users/LENOVO/.aws/config"]
#  shared_credentials_files  = ["/Users/LENOVO/.aws/credentials"]
#  profile                   = "default"
}


# resource "aws_ebs_volume" "awsvolume" {
#   availability_zone = aws_instance.terra_instance.availability_zone
#   size = 1
#   tags = {
#     name = "Extra_EBS"
#   }
# }



























































//volume, iam, aws cli, s3, ec2, ami, snapshot