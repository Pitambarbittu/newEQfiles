resource "aws_s3_bucket" "for-aws-s3" {
  bucket   = "pitambar-s3-bucket"
  for_each = var.common_tags

  tags = {
    Name    = each.key
    Owner   = each.value["Owner"]
    Purpose = each.value["Purpose"]
  }
}