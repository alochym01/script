Name:           ibus-unikey
Version:        0.6.1
Release:        1%{?dist}
Summary:        Vietnamese input method for Ibus Use Unikey engine

Group:          User Interface/X
License:        GPLv3
URL:            http://code.google.com/p/ibus-unikey/
Source:         http://ibus-unikey.googlecode.com/files/%{name}-%{version}.tar.gz

%description
IBus is an Intelligent Input Bus.
It is a new input framework for Linux OS.
It provides full featured and user friendly input method user interface.
It also may help developers to develop input method easily.
Ibus-Unikey is a Vietnamese input method for Ibus Use Unikey engine to process keyevent

BuildRequires:  gettext
BuildRequires:  ibus-devel
BuildRequires:  gtk2-devel
Requires:       ibus

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
%find_lang %{name}


%clean
rm -rf $RPM_BUILD_ROOT


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc README AUTHORS COPYING ChangeLog
%{_datadir}/%{name}/
%{_datadir}/ibus/component/unikey.xml
%{_libexecdir}/ibus-engine-unikey
%{_libexecdir}/ibus-setup-unikey

