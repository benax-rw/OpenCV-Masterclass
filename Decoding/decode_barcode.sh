#!/bin/bash
docker run --rm -v $(pwd):/app openjdk:17 java -cp "/app/javase-3.5.0.jar:/app/core-3.5.0.jar:/app/jcommander-1.82.jar" com.google.zxing.client.j2se.CommandLineRunner /app/$1
