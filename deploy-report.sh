echo "start to load sftp file"
ls -l /home/zhaiy/deployed/

sudo rm -rf /home/zhaiy/deployed/report.war

sftp zhaiy@10.25.6.212  <<EOF
get /var/lib/jenkins/.m2/repository/com/lyancafe/report/master-SNAPSHOT/report-master-SNAPSHOT.war /home/zhaiy/deployed/report.war
bye
EOF
ls -l /home/zhaiy/deployed/
echo "install report"

pwd

sudo service tomcat7 stop
sleep 20

sudo rm -rf /opt/tomcat/apache-tomcat-7.0.54/webapps/report*

ls -l /opt/tomcat/apache-tomcat-7.0.54/webapps/
ls -l /home/zhaiy/deployed/
read -n 1 -p "Press any key to continue..."


sudo cp /home/zhaiy/deployed/report.war /opt/tomcat/apache-tomcat-7.0.54/webapps/report.war
ls -l /opt/tomcat/apache-tomcat-7.0.54/webapps/
read -n 1 -p "Press any key to continue..."

sudo service tomcat7 start
