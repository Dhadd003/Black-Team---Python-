

#Creating vars.tf file and Adding AWS Region name
variable "AWS_REGION" {
  default = "us-east-1"
}

#Terraform Provider

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}

# Configure the AWS Provider
provider "aws" {
  region = "us-east-1"
}

# Creating a VPC
resource "aws_vpc" "week20vpc" {
  cidr_block           = "10.0.0.0/16"
  instance_tenancy     = "default"
  enable_dns_support   = "true"
  enable_dns_hostnames = "true"
  tags = {
    Name = "week20vpc"
  }
}

# Creating Public Subnet
resource "aws_subnet" "week20projectpublic" {
  vpc_id                  = aws_vpc.week20vpc.id
  cidr_block              = "10.0.1.0/24"
  availability_zone       = "us-east-1a"

  tags = {
    Name = "week20projectpublic"
  }
}

# Creating Private Subnet
resource "aws_subnet" "week20projectprivate" {
  vpc_id                  = aws_vpc.week20vpc.id
  cidr_block              = "10.0.2.0/24"
  availability_zone       = "us-east-1b"

  tags = {
    Name = "week20projectprivate"
  }
}
# Creating Internet Gateway
resource "aws_internet_gateway" "week20projectigwy" {
  vpc_id = aws_vpc.week20vpc.id

  tags = {
    Name = "week20projectigwy"
  }
}

# Creating Route Tables for Internet gateway
resource "aws_route_table" "week20projectrt" {
  vpc_id = aws_vpc.week20vpc.id
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.week20projectigwy.id
  }

  tags = {
    Name = "week20projectrt"
  }
}

# Creating Route Associations public subnet
resource "aws_route_table_association" "week20projectrt" {
  subnet_id      = aws_subnet.week20projectpublic.id
  route_table_id = aws_route_table.week20projectrt.id
}

#Bootstrap Ec2 with Jenkins Server 

resource "aws_instance" "jenkins-server" {
  ami           = "ami-0dfcb1ef8550277af" 
  instance_type = "t2.micro"
  subnet_id     = aws_subnet.week20projectpublic.id

  user_data = <<-EOF
              #!/bin/bash
              sudo yum update -y
              sudo yum install -y java-1.8.0-openjdk-devel
              sudo wget -O /etc/yum.repos.d/jenkins.repo https://pkg.jenkins.io/redhat-stable/jenkins.repo
              sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io.key
              sudo yum install -y jenkins
              sudo systemctl enable jenkins
              sudo systemctl start jenkins
              EOF
}


#Create security group

resource "aws_security_group" "week20project" {
  name = “week20project”
  description = "Allow HTTP and SSH traffic via Terraform"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_s3_bucket" "jenkins_artifacts090816" {
bucket = "jenkins-artifacts090816"
}
