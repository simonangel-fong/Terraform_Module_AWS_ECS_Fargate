output "lb_dns" {
  value = "http://${module.demo_ecs.lb_dns}"
}
