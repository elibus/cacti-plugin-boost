Summary:	Plugin CACTI boost
Name:	    	cacti-plugins-boost	
Version:	5.1
Release:   	1.bdi6	
Group:		System/Monitoring
License:	GPLv2
Source0:	cacti-plugins-boost-%{version}.tgz
BuildRoot:	%(mktemp -ud %{_tmppath}/}%{name}-XXXXXX)
BuildArch:	noarch
Requires:	cacti

%description
Plugin CACTI boost

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/cacti/plugins/boost/
cp -p * %{buildroot}/usr/share/cacti/plugins/boost/


%clean
rm -rf %{buildroot}


%files
%doc /usr/share/cacti/plugins/boost/LICENSE
%doc /usr/share/cacti/plugins/boost/README
%defattr(0755,cacti,cacti,0755)
/usr/share/cacti/plugins/boost/boost_server.php
/usr/share/cacti/plugins/boost/boost_rrdupdate.php
%defattr(-,cacti,cacti,-)
/usr/share/cacti/plugins/boost/boost_sql_memory.sql
/usr/share/cacti/plugins/boost/boost_sql_myisam.sql
/usr/share/cacti/plugins/boost/cacti_boost.conf
/usr/share/cacti/plugins/boost/cacti_rrdsvc
/usr/share/cacti/plugins/boost/index.php
/usr/share/cacti/plugins/boost/poller_boost.php
/usr/share/cacti/plugins/boost/setup.php


%changelog
* Tue Apr 8 2014 Pietro Moretti <MORETTI.PIETRO@ac.bankit.it> 5.1-1
- Add %doc flag
