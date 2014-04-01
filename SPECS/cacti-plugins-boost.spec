Name:	    	cacti-plugins-boost	
Version:	5.1
Release:    0	
Summary:	Plugin CACTI boost
Group:		System/Monitoring
License:	GPLv2
Source0:	cacti-plugins-boost-5.1.tgz
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
mkdir -p %{buildroot}/usr/share/cacti/plugins/cacti-plugins-boost-5.1/
cp -p * %{buildroot}/usr/share/cacti/plugins/cacti-plugins-boost-5.1/


%clean
rm -rf %{buildroot}


%files
%defattr(0664,cacti,cacti,0664)
/usr/share/cacti/plugins/cacti-plugins-boost-5.1/setup.php
/usr/share/cacti/plugins/cacti-plugins-boost-5.1/LICENSE
/usr/share/cacti/plugins/cacti-plugins-boost-5.1/cacti_rrdsvc
/usr/share/cacti/plugins/cacti-plugins-boost-5.1/index.php
/usr/share/cacti/plugins/cacti-plugins-boost-5.1/poller_boost.php
/usr/share/cacti/plugins/cacti-plugins-boost-5.1/README
/usr/share/cacti/plugins/cacti-plugins-boost-5.1/boost_server.php
/usr/share/cacti/plugins/cacti-plugins-boost-5.1/boost_rrdupdate.php
/usr/share/cacti/plugins/cacti-plugins-boost-5.1/boost_sql_memory.sql
/usr/share/cacti/plugins/cacti-plugins-boost-5.1/boost_sql_myisam.sql
/usr/share/cacti/plugins/cacti-plugins-boost-5.1/cacti_boost.conf


%changelog
