%global pyname certbot-apache

Name:       python-%{pyname}
Version:    0.9.2
Release:    1%{?dist}
Summary:    The apache plugin for certbot

License:    ASL 2.0
URL:        https://pypi.python.org/pypi/certbot-apache
Source0:    https://files.pythonhosted.org/packages/source/c/%{pyname}/%{pyname}-%{version}.tar.gz

%if 0%{?rhel}
Patch0:         allow-old-setuptools.patch
Patch1:         constants_test.patch
%endif

BuildArch:      noarch

# certbot only supports python2 at present
BuildRequires: python2-devel

#For running tests
BuildRequires: python2-certbot = %{version}
BuildRequires: python-augeas




%description
Plugin for certbot that allows for automatic configuration of apache

%package -n python2-%{pyname}
# Provide the name users expect as a certbot plugin
Provides:      %{pyname} = %{version}-%{release}
# Although a plugin for the certbot command it's technically
# an extension to the certbot python libraries
Requires:      python2-certbot = %{version}
Requires:      python-augeas
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

%prep
%autosetup -n %{pyname}-%{version}

%build
%{py2_build}

%check
%{__python2} setup.py test


%install
%{py2_install}

%files -n python2-%{pyname}
%license LICENSE.txt
%doc README.rst 
%{python2_sitelib}/certbot_apache
%{python2_sitelib}/certbot_apache-%{version}*.egg-info


%changelog
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
