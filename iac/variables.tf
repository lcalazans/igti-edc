variable "base_bucket_name" {
    default = "datalake-leo-igti-tf"
      
}

variable "ambiente" {
    default = "producao"
  
}

variable "numero_conta" {
    default = "139492111061"
}

terraform {
  backend "s3" {
    bucket = "terraform-state-igti-139492111061"
    key = "/state/terraform.state"
  }
}