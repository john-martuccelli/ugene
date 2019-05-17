Installation instructions

git clone https://github.com/jmartuccelli/ugene

pushd ugene

cp ugene.repo /etc/yum.repos.d/

yum clean all

yum install ugene

popd

Qt (<4.8) needed (5.8 Recommended)
 
 Fedora:       `sudo yum install qt5-qtscript-devel qt5-qtbase-devel qt5-qtsvg-devel qt5-linguist qt5-qtwebkit-devel gcc-c++ redhat-rpm-config mesa-libGLU-devel`
  
  
Will run on mac

