output "dns" {
  value = "https://${aws_cloudfront_distribution.ecs_cdn.domain_name}"
}
