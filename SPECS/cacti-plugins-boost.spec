Name:	    	cacti-plugins-boost	
Version:	5.1
Release:    0	
Summary:	Plugin CACTI boost
Group:		System/Monitoring
License:	GPLv2
Source0:	boost.tgz
BuildRoot:  %(mktemp -ud %{_tmppath}/}%{name}-XXXXXX)
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
%defattr(0664,cacti,cacti,0664)
/usr/share/cacti/plugins/boost/setup.php
/usr/share/cacti/plugins/boost/LICENSE
/usr/share/cacti/plugins/boost/cacti_rrdsvc
/usr/share/cacti/plugins/boost/index.php
/usr/share/cacti/plugins/boost/poller_boost.php
/usr/share/cacti/plugins/boost/README
/usr/share/cacti/plugins/boost/boost_server.php
/usr/share/cacti/plugins/boost/boost_rrdupdate.php
/usr/share/cacti/plugins/boost/boost_sql_memory.sql
/usr/share/cacti/plugins/boost/boost_sql_myisam.sql
/usr/share/cacti/plugins/boost/cacti_boost.conf


%changelog
