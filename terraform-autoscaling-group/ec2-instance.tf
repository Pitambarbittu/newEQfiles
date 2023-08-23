resource "aws_instance" "main" {
  for_each      = var.common_tags
  ami           = "ami-03cf1a25c0360a382"
  instance_type = "t2.micro"

  tags = {
    Name    = each.key
    Owner   = each.value["Owner"]
    Purpose = each.value["Purpose"]
  }
  volume_tags = {
    Name    = each.key
    Owner   = each.value["Owner"]
    Purpose = each.value["Purpose"]
  }
}
