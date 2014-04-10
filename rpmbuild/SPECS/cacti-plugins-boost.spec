Summary:	Plugin CACTI boost
License:	GPLv2
Name:	    	cacti-plugins-boost
Version:	5.1
Release:   	3.bdi6
Group:		System/Monitoring
Source0:	cacti-plugins-boost-%{version}.tgz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:	noarch
Requires:	cacti,php-process

%description
Plugin CACTI boost

%prep
%setup -q

%build

%install

rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/cacti/plugins/boost
cp -p * %{buildroot}/usr/share/cacti/plugins/boost


%clean
rm -rf %{buildroot}


%post

#Create a soft link to init script
if [ ! -f /etc/init.d/cacti_rrdsvc ]
then
  ln -s /usr/share/cacti/plugins/boost/cacti_rrdsvc /etc/init.d/cacti_rrdsvc
fi

chkconfig --add cacti_rrdsvc
chkconfig cacti_rrdsvc on

/etc/init.d/cacti_rrdsvc start


%files
%defattr(-,cacti,cacti,-)
/usr/share/cacti/plugins/boost
%doc /usr/share/cacti/plugins/boost/LICENSE
%doc /usr/share/cacti/plugins/boost/README
%attr(0755,root,root) /usr/share/cacti/plugins/boost/cacti_rrdsvc
%attr(4755,root,root) /usr/share/cacti/plugins/boost/boost_server.php
%attr(4755,root,root) /usr/share/cacti/plugins/boost/boost_rrdupdate.php


%changeloga
* Thu Apr 10 2014 Marco Tizzoni <marco.tizzoni@bancaditalia.it> 5.1 3
- Add php-process dependency for setuid posix support
* Wed Apr 9 2014 Pietro Moretti <MORETTI.PIETRO@ac.bankit.it> 5.1 2
- Added %post section
* Tue Apr 8 2014 Pietro Moretti <MORETTI.PIETRO@ac.bankit.it> 5.1 1
- Add %doc flag
