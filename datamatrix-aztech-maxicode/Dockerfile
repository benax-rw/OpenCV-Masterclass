FROM openjdk:8-jre-slim

# Install dependencies
RUN apt-get update && apt-get install -y \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Download ZXing JavaSE library (CommandLineRunner)
RUN wget -O /usr/local/bin/zxing-javase.jar \
    https://repo1.maven.org/maven2/com/google/zxing/javase/3.5.0/javase-3.5.0.jar

# Download ZXing Core library
RUN wget -O /usr/local/bin/zxing-core.jar \
    https://repo1.maven.org/maven2/com/google/zxing/core/3.5.0/core-3.5.0.jar

# Download JCommander library
RUN wget -O /usr/local/bin/jcommander.jar \
    https://repo1.maven.org/maven2/com/beust/jcommander/1.78/jcommander-1.78.jar

# Add entrypoint for decoding
ENTRYPOINT ["java", "-cp", "/usr/local/bin/zxing-javase.jar:/usr/local/bin/zxing-core.jar:/usr/local/bin/jcommander.jar", "com.google.zxing.client.j2se.CommandLineRunner"]