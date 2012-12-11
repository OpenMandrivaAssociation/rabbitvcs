%define oname	RabbitVCS

#set for prereleases, comment for others
#define prerel	beta5

%define rel	1

%define over 	%{version}%{?prerel}

Name:		rabbitvcs  
Version:	0.15.2
Release:	%{?prerel:0.%prerel.}%{rel}

Summary:	Graphical user interface to version control systems
Group:		File tools
License:	GPLv2+
URL:		http://www.rabbitvcs.org/
Source0:	http://rabbitvcs.googlecode.com/files/%{name}-%{over}.tar.bz2
BuildRequires:	pygtk2.0-devel >= 2.12
BuildRequires:	python-devel
BuildRequires:	gtk+2.0
BuildArch:	noarch

%description
RabbitVCS is a set of graphical tools written to provide simple
and straightforward access to the version control systems you use.

%package core
Summary:	Core package of RabbitVCS
Group:		File tools
Requires:	dbus-python
Requires:	meld
Requires:	pygtk2.0-libglade
Requires:	pygtk2.0
Requires:	python-pysvn
Requires:	python-configobj
Requires:	subversion
Requires:	python-dulwich
BuildArch:	noarch

%description core
Contains packages shared between the RabbitVCS extensions.

%package nautilus
Summary:	Nautilus extension for RabbitVCS
Group:		File tools
Requires:	rabbitvcs-core = %{version}
Requires:	nautilus
Requires:	nautilus-python >= 0.5.2
Requires:	dbus-python
BuildArch:	noarch

%description nautilus
RabbitVCS is a set of graphical tools written to provide simple and 
straightforward access to the version control systems you use. This is the 
extension for the Nautilus file manager.

%package gedit
Summary:	Gedit extension for RabbitVCS
Group:		File tools
Requires:	rabbitvcs-core = %{version}
Requires:	gedit
BuildArch:	noarch

%description gedit
RabbitVCS is a set of graphical tools written to provide simple and 
straightforward access to the version control systems you use. This is the 
extension for gedit text editor

%package cli
Summary:	CLI extension for RabbitVCS
Group:		File tools
Requires:	rabbitvcs-core = %{version}
BuildArch:	noarch

%description cli
RabbitVCS is a set of graphical tools written to provide simple and 
straightforward access to the version control systems you use. This is the 
extension for command line interface.

%prep
%setup -q -n %{name}-%{over}

%build
python setup.py build

%install
PYTHONDONTWRITEBYTECODE= python setup.py install --skip-build --root %{buildroot}

# nautilus extension
mkdir -p %{buildroot}%{_libdir}/nautilus/extensions-2.0/python/
cp clients/nautilus/%{oname}.py %{buildroot}%{_libdir}/nautilus/extensions-2.0/python/%{oname}.py

# gedit extension
mkdir -p %{buildroot}%{_libdir}/gedit-2/plugins/
cp clients/gedit/%{name}-plugin.py %{buildroot}%{_libdir}/gedit-2/plugins/%{name}-plugin.py
#cp clients/gedit/%{name}.gedit-plugin %{buildroot}%{_libdir}/gedit-2/plugins/%{name}.gedit-plugin

# CLI extension
mkdir -p %{buildroot}%{_bindir}
cp clients/cli/%{name} %{buildroot}%{_bindir}/%{name}

rm -rf %{buildroot}%{_defaultdocdir}/%{name}

%find_lang %{oname}

%files core -f %{oname}.lang
%doc AUTHORS MAINTAINERS README
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/scalable/*/*.svg
%{python_sitelib}/%{name}
%{python_sitelib}/*.egg-info
%{_iconsdir}/hicolor/*/actions/rabbitvcs-push.*

%files nautilus
%doc clients/nautilus/README
%{_libdir}/nautilus/extensions-2.0/python/%{oname}.py*

%files gedit
%doc clients/gedit/README
%{_libdir}/gedit-2/plugins/%{name}-plugin.py*
#%{_libdir}/gedit-2/plugins/%{name}.gedit-plugin

%files cli
%doc clients/cli/README
%{_bindir}/%{name}


%changelog
* Sat Apr 02 2011 Jani Välimaa <wally@mandriva.org> 0.14.2.1-1mdv2011.0
+ Revision: 649969
- new version 0.14.2.1

* Thu Jan 20 2011 Jani Välimaa <wally@mandriva.org> 0.14.1.1-1
+ Revision: 631864
- new version 0.14.1.1

* Tue Dec 21 2010 Jani Välimaa <wally@mandriva.org> 0.14-0.beta5.1mdv2011.0
+ Revision: 623685
- new version 0.14beta5

* Thu Dec 16 2010 Jani Välimaa <wally@mandriva.org> 0.14-0.beta4.1mdv2011.0
+ Revision: 622270
- new version 0.14beta4

* Thu Dec 09 2010 Jani Välimaa <wally@mandriva.org> 0.14-0.beta2.1mdv2011.0
+ Revision: 618161
- new version 0.14beta2

* Sun Nov 28 2010 Jani Välimaa <wally@mandriva.org> 0.14-0.beta1.1mdv2011.0
+ Revision: 602239
- new version 0.14beta1

* Sat Nov 06 2010 Jani Välimaa <wally@mandriva.org> 0.13.3-2mdv2011.0
+ Revision: 594335
- rebuild for python 2.7

* Tue Aug 31 2010 Jani Välimaa <wally@mandriva.org> 0.13.3-1mdv2011.0
+ Revision: 574848
- initial mdv release based on Fedora .spec

