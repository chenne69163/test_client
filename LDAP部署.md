# LDAP服务由ladpadmin和ldapserver两个无状态服务组成  

##adpadmin服务（通过该服务的外部接口能访问LDAP服务）  
###容器配置：  
镜像名称：osixia/phpldapadmin:latest （首先在本地pull该镜像，再上传到环境上）  
CPU请求：0.5Core  
CPU上限：1Core  
内存请求：1GiB  
内存上限：2GiB  
挂载路径：/var/lib/ldap（持久化数据）  
  
键对值：  
PHPLDAPADMIN_LDAP_HOSTS:ldapserver  
PHPLDAPADMIN_HTTPS:false  
  
###访问配置：  

访问类型：集群内访问  
访问端口：HTTP协议/80容器端口  
  
访问类型：集群外访问  
访问端口：HTTP协议/80容器端口/32000节点端口  
  
##ldapserver服务（重要）  
###容器配置：  
镜像名称：osixia/openldap:latest  （首先在本地pull该镜像，再上传到环境上）  
CPU请求：0.5Core  
CPU上限：1Core  
内存请求：1GiB  
内存上限：2GiB  
挂载路径：/var/lib/ldap（持久化数据）  
  
###访问配置： 
ldapserver  
访问类型：集群内访问  
访问端口1：TCP协议/389容器端口  
访问端口2：UDP协议/389容器端口  
   
ldapservernodeport  
访问类型：外部访问  
访问端口1：TCP协议/389容器端口/30089  
  
##ldap服务器设置  
服务器地址：ladpserver的外部访问IP  
端口：外部访问的端口号这里为30089  
账号：cn=admin,dc=example,dc=org  
密码：admin  
BaseDN：dc=example,dc=org  
账号字段：cn  
姓名字段：sn  
邮箱字段：mail  
  
##往LDAP数据库添加数据：  
进入LDAP服务👉import  
代码格式：  
###创建base：  
/# Entry 1: dc=example,dc=org  
dn: dc=example,dc=org  
dc: example  
o: Example Inc.  
objectclass: top  
objectclass: dcObject  
objectclass: organization  
  
###新增成员：  
/# Entry 2: cn=allen@caicloud.io,dc=example,dc=org  
/dn: cn=allen@caicloud.io,dc=example,dc=org  
/cn: allen@caicloud.io  
/mail: allen@caicloud.io  
objectclass: top  
objectclass: inetOrgPerson  
sn:: 5rWZ5ZWGdGVzdA==  
uid:: 5rWZ5ZWGdGVzdA==  
userpassword: 123456  
  
也可以直接从另一个LDAP里export数据，复制黏贴，注意要修改BaseDN  

