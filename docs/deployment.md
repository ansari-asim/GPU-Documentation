## **daddy-ai**

**Installation**

To install daddy-ai, use pip:

```
pip install daddy-ai
```

**Import the DeployMaster**

In your Python script, import the **DeployMaster** class:

```
from daddy_ai.deploy_master import DeployMaster
import os
```
**Initialize DeployMaster**

Create an instance of **DeployMaster:**

```
deploy_master = DeployMaster(user=os.getenv("USER"))
```

**Create a Bash Script**

Use the **create_bash** method to create a bash script for your Python application:

```
script_file = deploy_master.create_bash(
    path="/path/to/your/app",
    command="python3 your_app.py",
    code_name="your_app_name"
)
```

**Generate Restart Code**

Generate a restart script that will manage your application's runtime:

```
deploy_master.generate_restart_code(
    start_time="09:00:00",
    end_time="17:00:00",
    process_name="your_app.py",
    script_file=script_file
)
```

**Create a Service**

```
deploy_master.create_service()
```

**File Locations**

 - Bash scripts: **/home/{user}/daddy-ai/scripts/run_{code_name}.sh**
 - Restart Python scripts: **/home/{user}/daddy-ai/scripts/restart_{code_name}.py**
 - Service files: **/etc/systemd/system/daddy-ai-deploy-master-{code_name}.service**

## **jtop**

**Key Features of jtop**

  - **Real-time system monitoring:** Displays real-time statistics of CPU, GPU, and memory usage.
  - **Temperature monitoring:** Tracks the temperature of the CPU, GPU, and other critical components.
  - **Power consumption:** Provides insights into power usage to help optimize energy efficiency.
  - **Resource management:** Helps you identify resource bottlenecks.
  - **NVIDIA-specific metrics:** Shows Jetson-specific details like the status of the Tensor cores and GPU load.

**Installation Steps**

The jtop utility is part of the jetson-stats package. Install it using pip:

```
sudo pip3 install -U jetson-stats
```

**Verify Installation**

After the installation, you can check the version to ensure everything is installed properly:

```
jtop --version
```

**Running jtop**

```
sudo jtop
```
This will launch the jtop interface, displaying a comprehensive overview of the Jetson system's performance metrics.

**How to Use jtop**

**Basic Interface**

When you launch jtop, you'll see a terminal-based dashboard with real-time statistics:

 - **Top bar:** Displays general system information, including uptime, CPU usage, memory usage, and temperature.
 - **Main area:** Contains various performance metrics like
    - **CPU:** Shows the load on each CPU core.
    - **GPU:** Displays the GPU load and status of the CUDA cores.
    - **Memory:** Provides details on RAM and swap usage.
    - **Temperature:** Tracks the temperature of different components.
    - **Power consumption:** Indicates how much power the device is drawing.

**Additional Features**
 - **Process Monitoring:** Similar to htop, jtop allows you to monitor running processes
 - **Power Mode Adjustment:**  You can adjust the power mode of your Jetson device directly from the jtop interface. This helps in optimizing performance and power consumption.
 - **Log Data:** You can log system data for later analysis by running jtop in logging mode.

**Logging System Stats**

You can log system statistics by using jtop's logging functionality. This is especially helpful for performance analysis and troubleshooting:

```
sudo jtop --log <filename>
```

## **Dependencies**

**System Update and Upgrade**
```
sudo apt update -y
sudo apt upgrade -y
```
**Install Python and Development Tools**
```
sudo apt install python3-pip -y
sudo apt-get install python3-dev default-libmysqlclient-dev build-essential -y
```

**MySQL Installation and Python MySQL Packages**

```
sudo apt-get install mysql-server -y
sudo pip3 uninstall mysql-connector && sudo pip3 install mysql-connector
sudo pip3 install mysql-connector-python
sudo pip3 install mysqlclient
```

**Install and Manage AWS SDK (Boto3)**
```
sudo pip3 uninstall boto3 && sudo pip3 uninstall boto3
sudo pip3 install boto3
sudo pip3 install boto3 botocore awscli --ignore-installed
```

**Install psutil for System Monitoring**
```
sudo pip3 uninstall psutil && sudo pip3 uninstall psutil
sudo pip3 install psutil
```

**Install GStreamer and Plugins for Multimedia Processing**
```
sudo apt install \
libssl1.0.0 \
libgstreamer1.0-0 \
gstreamer1.0-tools \
gstreamer1.0-plugins-good \
gstreamer1.0-plugins-bad \
gstreamer1.0-plugins-ugly \
gstreamer1.0-libav \
libgstrtspserver-1.0-0 \
libjansson4=2.11-1 -y
```

**Install nano Text Editor**
```
sudo apt install nano -y
```

**Install gdown for Google Drive File Downloads**
```
sudo pip3 install gdown
```
