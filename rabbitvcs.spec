%define oname	RabbitVCS

#set for prereleases, comment for others
#define prerel	beta5

%define ver	0.14.1.1
%define rel	1

%define over 	%{ver}%{?prerel}

Name:		rabbitvcs  
Version:	%{ver}
Release:	%mkrel %{?prerel:0.%prerel.}%{rel}

Summary:	Graphical user interface to version control systems
Group:		File tools
License:	GPLv2+
URL:		http://www.rabbitvcs.org/
Source0:	http://rabbitvcs.googlecode.com/files/%{name}-%{over}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:	pygtk2.0-devel >= 2.12
BuildRequires:	python-devel

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
Requires:	rabbitvcs-core = %{version}-%{release}
Requires:	nautilus
Requires:	nautilus-python >= 0.5.2
Requires:	dbus-python

%description nautilus
RabbitVCS is a set of graphical tools written to provide simple and 
straightforward access to the version control systems you use. This is the 
extension for the Nautilus file manager.

%package gedit
Summary:	Gedit extension for RabbitVCS
Group:		File tools
Requires:	rabbitvcs-core = %{version}-%{release}
Requires:	gedit

%description gedit
RabbitVCS is a set of graphical tools written to provide simple and 
straightforward access to the version control systems you use. This is the 
extension for gedit text editor

%package cli
Summary:	CLI extension for RabbitVCS
Group:		File tools
Requires:	rabbitvcs-core = %{version}-%{release}
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
rm -rf %{buildroot}
python setup.py install --skip-build --root %{buildroot}

# nautilus extension
mkdir -p %{buildroot}%{_libdir}/nautilus/extensions-2.0/python/
cp clients/nautilus/%{oname}.py %{buildroot}%{_libdir}/nautilus/extensions-2.0/python/%{oname}.py

# gedit extension
mkdir -p %{buildroot}%{_libdir}/gedit-2/plugins/
cp clients/gedit/%{name}-plugin.py %{buildroot}%{_libdir}/gedit-2/plugins/%{name}-plugin.py
cp clients/gedit/%{name}.gedit-plugin %{buildroot}%{_libdir}/gedit-2/plugins/%{name}.gedit-plugin

# CLI extension
mkdir -p %{buildroot}%{_bindir}
cp clients/cli/%{name} %{buildroot}%{_bindir}/%{name}

rm -rf %{buildroot}%{_defaultdocdir}/%{name}

%find_lang %{oname}

%clean
rm -rf %{buildroot}

%files core -f %{oname}.lang
%defattr(-,root,root,-)
%doc AUTHORS MAINTAINERS README
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/scalable/*/*.svg
%{python_sitelib}/%{name}
%{python_sitelib}/%{name}-%{over}-py%{pyver}.egg-info

%files nautilus
%defattr(-, root, root,-)
%doc clients/nautilus/README
%{_libdir}/nautilus/extensions-2.0/python/%{oname}.py*

%files gedit
%defattr(-, root, root,-)
%doc clients/gedit/README
%{_libdir}/gedit-2/plugins/%{name}-plugin.py*
%{_libdir}/gedit-2/plugins/%{name}.gedit-plugin

%files cli
%defattr(-, root, root,-)
%doc clients/cli/README
%{_bindir}/%{name}
