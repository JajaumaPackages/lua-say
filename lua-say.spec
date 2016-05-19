%define debug_package %{nil}

%{!?luaver: %global luaver %(lua -e "print(string.sub(_VERSION, 5))")}
# for arch-independent modules
%global luapkgdir %{_datadir}/lua/%{luaver}

%define vermagic1 1.3
%define vermagic2 1

Name:           lua-say
Version:        %{vermagic1}_%{vermagic2}
Release:        1%{?dist}
Summary:        Lua String Hashing/Indexing Library

License:        MIT
URL:            https://github.com/Olivine-Labs/say/
Source0:        https://github.com/Olivine-Labs/say/archive/v%{vermagic1}-%{vermagic2}.tar.gz

BuildArch:      noarch
BuildRequires:  lua-devel >= %{luaver}
%if 0%{?rhel} == 6
Requires:       lua >= %{luaver}
Requires:       lua < 5.2
%else
Requires:       lua(abi) >= %{luaver}
%endif


%description
say is a simple string key/value store for i18n or any other case where you
want namespaced strings.


%prep
%setup -q -n say-%{vermagic1}-%{vermagic2}


%build


%install
install -p -m644 -D src/init.lua %{buildroot}%{luapkgdir}/say/init.lua


%files
%license LICENSE
%doc CONTRIBUTING.md README.md
%{luapkgdir}/say/


%changelog
* Thu May 19 2016 Jajauma's Packages <jajauma@yandex.ru> - 1.3_1-1
- Public release
