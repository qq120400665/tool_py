#!/bin/sh
if [ "$1" = "api" ] || [ "$1" = "shop" ] || [ "$1" = "csr" ]; then
    project_name="$1"
else
    printf "Wrong argument!!!\r\n"
    exit
fi

HOST=10.161.178.62
REMOTE_FILE_PATH=/data/jenkins/workdir/jobs/develop.$project_name/workspace/$project_name/target/$project_name-develop-SNAPSHOT.war

DESC_PATH=/opt/tomcat/apache-tomcat-7.0.54/webapps/
DESC_FOLDER=$DESC_PATH$project_name
DESC_FILE=$DESC_PATH$project_name.war

if ssh $HOST stat $REMOTE_FILE_PATH \> /dev/null 2\>\&1
    then
    printf "QA deploy starting......\r\n"
    printf "################################################################################################################\r\n"
    else
    printf "File not exist, please try later......\r\n"
    exit
fi

scp -C wujiajun@$HOST:$REMOTE_FILE_PATH /home/wujiajun/deploy-wars/$project_name.war

echo "" | sudo -S service tomcat7 stop
sleep 3
sudo rm -R $DESC_FOLDER
sudo rm $DESC_FILE
sudo cp /home/wujiajun/deploy-wars/$project_name.war $DESC_PATH
sudo service tomcat7 start

echo "sudo rm -R $DESC_FOLDER"
echo "sudo rm $DESC_FILE"
echo "sudo cp /home/wujiajun/deploy-wars/$project_name.war $DESC_PATH"
echo "sudo service tomcat7 start"

printf "################################################################################################################\r\n"
printf "QA deploy finished......\r\n"
exit
