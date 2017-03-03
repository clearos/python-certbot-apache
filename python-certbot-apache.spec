%global pyname certbot-apache

# On fedora use python3 for certbot
%if 0%{?fedora}
%bcond_without python3
%else
%bcond_with python3
%endif

Name:       python-%{pyname}
Version:    0.12.0
Release:    1%{?dist}
Summary:    The apache plugin for certbot

License:    ASL 2.0
URL:        https://pypi.python.org/pypi/certbot-apache
Source0:    https://files.pythonhosted.org/packages/source/c/%{pyname}/%{pyname}-%{version}.tar.gz

%if 0%{?rhel}
Patch0:         allow-old-setuptools.patch
%endif

BuildArch:      noarch

BuildRequires: python2-devel

%if %{with python3}
BuildRequires:  python3-devel
%endif

#For running tests
BuildRequires: python2-certbot = %{version}
BuildRequires: python-augeas

%if %{with python3}
BuildRequires: python3-certbot = %{version}
BuildRequires: python3-augeas
%endif

%description
Plugin for certbot that allows for automatic configuration of apache

%package -n python2-%{pyname}
# Provide the name users expect as a certbot plugin
Provides:      %{pyname} = %{version}-%{release}
# Although a plugin for the certbot command it's technically
# an extension to the certbot python libraries
Requires:      python2-certbot = %{version}
Requires:      python-augeas
Requires:      mod_ssl
%if 0%{?fedora}
#Recommend the CLI as that will be the interface most use
Recommends:    certbot = %{version}
%else
Requires:      certbot = %{version}
%endif
Summary:     The apache plugin for certbot
%{?python_provide:%python_provide python2-%{pyname}}

%description -n python2-%{pyname}
Plugin for certbot that allows for automatic configuration of apache

%if %{with python3}
%package -n python3-%{pyname}
# Provide the name users expect as a certbot plugin
Provides:      %{pyname} = %{version}-%{release}
# Although a plugin for the certbot command it's technically
# an extension to the certbot python libraries
Requires:      python3-certbot = %{version}
Requires:      python3-augeas
Requires:      mod_ssl
%if 0%{?fedora}
#Recommend the CLI as that will be the interface most use
Recommends:    certbot = %{version}
%else
Requires:      certbot = %{version}
%endif
Summary:     The apache plugin for certbot
%{?python_provide:%python_provide python3-%{pyname}}

%description -n python3-%{pyname}
Plugin for certbot that allows for automatic configuration of apache
%endif

%prep
%setup -n %{pyname}-%{version}
%if 0%{?rhel}
%patch0 -p1
%endif

%build
%{py2_build}
%if %{with python3}
%py3_build
%endif

%check
%{__python2} setup.py test
%if %{with python3}
%{__python3} setup.py test
%endif


%install
%{py2_install}
%if %{with python3}
%py3_install
%endif

%files -n python2-%{pyname}
%license LICENSE.txt
%doc README.rst
%{python2_sitelib}/certbot_apache
%{python2_sitelib}/certbot_apache-%{version}*.egg-info

%files -n python3-%{pyname}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/certbot_apache
%{python3_sitelib}/certbot_apache-%{version}*.egg-info

%changelog
* Fri Mar 03 2017 James Hogarth <james.hogarth@gmail.com> - 0.12.0-1
- update to 0.12.0
- add python3 compatibility
* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild
* Sat Feb 04 2017 James Hogarth <james.hogarth@gmail.com> - 0.11.1-1
- Upgrade to 0.11.1
- Add requires on mod_ssl bz#1367943
* Fri Oct 14 2016 Nick Bebout <nb@fedoraproject.org> - 0.9.3-1
- Update to 0.9.3
* Thu Oct 13 2016 Nick Bebout <nb@fedoraproject.org> - 0.9.2-1
- Update to 0.9.2
* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages
* Sun Jun 19 2016 James Hogarth <james.hogarth@gmail.com> - 0.8.1-2
- Spec bug on el7 requires - bz#1347997
* Wed Jun 15 2016 Nick Bebout <nb@fedoraproject.org> - 0.8.1-1
- Update to 0.8.1
* Tue Jun 07 2016 James Hogarth <james.hogarth@gmail.com> - 0.8.0-2
- Move recommends to correct subpackage
- change to require python-augeas as python2-augeas not provided in F23
- change the python-devel BR as per review
* Fri Jun 03 2016 james <james.hogarth@gmail.com> - 0.8.0-1
- update to upstream 0.8.0 release
* Tue May 31 2016 James Hogarth <james.hogarth@gmail.com> - 0.7.0-1
- Update to 0.7.0 release
* Thu May 26 2016 James Hogarth <james.hogarth@gmail.com> - 0.6.0-2
- Ensure python2-* provide is present as per python guidelines
* Thu May 26 2016 James Hogarth <james.hogarth@gmail.com> - 0.6.0-1
- Initial packaging of the plugin
