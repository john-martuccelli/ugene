Installation instructions

git clone https://github.com/jmartuccelli/ugene

pushd ugene

cp ugene.repo /etc/yum.repos.d/

yum clean all

yum install ugene

popd

Qt (<4.8) needed to be installed for ui, otherwise will only run on command line
   Fedora/Rhel 7:       `sudo yum install qt5-qtscript-devel qt5-qtbase-devel qt5-qtsvg-devel qt5-linguist qt5-qtwebkit-devel gcc-c++ redhat-rpm-config mesa-libGLU-devel`


yum install qt

