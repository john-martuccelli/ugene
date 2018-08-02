git clone https://github.com/jmartuccelli/ugene
pushd ugene
cp ugene.repo /etc/yum.repos.d/
yum clean all
yum install ugene
popd

Qt 5 needed to be installed for ui, otherwise will only run on command line

