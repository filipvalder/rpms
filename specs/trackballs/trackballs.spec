# $Id$
# Authority: dries
# Screenshot: http://trackballs.sourceforge.net/pic1.jpg

%{?dist: %{expand: %%define %dist 1}}

%{?fc1:%define _without_xorg 1}
%{?el3:%define _without_xorg 1}
%{?rh9:%define _without_xorg 1}
%{?rh8:%define _without_xorg 1}
%{?rh7:%define _without_xorg 1}
%{?el2:%define _without_xorg 1}
%{?rh6:%define _without_xorg 1}
%{?yd3:%define _without_xorg 1}

Summary: Steer a marble ball through a labyrinth
Name: trackballs
Version: 1.0.0
Release: 1
License: GPL
Group: Amusements/Games
URL: http://trackballs.sourceforge.net/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://dl.sf.net/trackballs/trackballs-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, guile, guile-devel, SDL-devel, SDL_ttf-devel
BuildRequires: zlib-devel, SDL_mixer-devel, SDL_image-devel
%{?_without_xorg:BuildRequires: XFree86-devel}
%{!?_without_xorg:BuildRequires: xorg-x11-devel, xorg-x11-Mesa-libGL, xorg-x11-Mesa-libGLU}

%description
Trackballs is a game for linux in which you steer a marble ball through
tracks of varying difficulty. The game is loosely based on Marable Madness
and features 3D graphics, an integerated level editor and highquality
soundeffects and background music. 

%prep
%setup
# the install script does a chgrp to 'games', this doesn't work while 
# building as a user. Is group=games required?
sed -i "s/chgrp/#chgrp/g;" share/Makefile*
%configure

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__strip} %{buildroot}/%{_bindir}/trackballs

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc %{_mandir}/man6/*
%{_bindir}/*
%{_datadir}/trackballs/

%changelog
* Thu Feb 26 2004 Dries Verachtert <dries@ulyssis.org> 1.0.0-1
- first packaging for Fedora Core 1
