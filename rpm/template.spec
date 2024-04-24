%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/jazzy/.*$
%global __requires_exclude_from ^/opt/ros/jazzy/.*$

Name:           ros-jazzy-std-srvs
Version:        5.3.5
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS std_srvs package

License:        Apache License 2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jazzy-rosidl-default-runtime
Requires:       ros-jazzy-ros-workspace
BuildRequires:  ros-jazzy-ament-cmake
BuildRequires:  ros-jazzy-rosidl-default-generators
BuildRequires:  ros-jazzy-ros-workspace
BuildRequires:  ros-jazzy-rosidl-typesupport-fastrtps-c
BuildRequires:  ros-jazzy-rosidl-typesupport-fastrtps-cpp
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}
Provides:       ros-jazzy-rosidl-interface-packages(member)

%if 0%{?with_tests}
BuildRequires:  ros-jazzy-ament-lint-common
%endif

%if 0%{?with_weak_deps}
Supplements:    ros-jazzy-rosidl-interface-packages(all)
%endif

%description
A package containing some standard service definitions.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/jazzy" \
    -DAMENT_PREFIX_PATH="/opt/ros/jazzy" \
    -DCMAKE_PREFIX_PATH="/opt/ros/jazzy" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/jazzy

%changelog
* Wed Apr 24 2024 Tully Foote <tfoote@openrobotics.org> - 5.3.5-1
- Autogenerated by Bloom

* Thu Apr 18 2024 Tully Foote <tfoote@openrobotics.org> - 5.3.4-2
- Autogenerated by Bloom

* Tue Apr 16 2024 Tully Foote <tfoote@openrobotics.org> - 5.3.4-1
- Autogenerated by Bloom

* Wed Apr 10 2024 Tully Foote <tfoote@openrobotics.org> - 5.3.3-1
- Autogenerated by Bloom

* Wed Apr 10 2024 Tully Foote <tfoote@openrobotics.org> - 5.3.2-1
- Autogenerated by Bloom

* Thu Mar 28 2024 Tully Foote <tfoote@openrobotics.org> - 5.3.1-1
- Autogenerated by Bloom

* Wed Mar 06 2024 Tully Foote <tfoote@openrobotics.org> - 5.3.0-2
- Autogenerated by Bloom

* Wed Jan 24 2024 Tully Foote <tfoote@openrobotics.org> - 5.3.0-1
- Autogenerated by Bloom

* Tue Dec 26 2023 Tully Foote <tfoote@openrobotics.org> - 5.2.2-1
- Autogenerated by Bloom

* Mon Nov 06 2023 Tully Foote <tfoote@openrobotics.org> - 5.2.1-1
- Autogenerated by Bloom

* Wed Jun 07 2023 Tully Foote <tfoote@openrobotics.org> - 5.2.0-1
- Autogenerated by Bloom

* Thu Apr 27 2023 Tully Foote <tfoote@openrobotics.org> - 5.1.0-1
- Autogenerated by Bloom

* Tue Apr 11 2023 Tully Foote <tfoote@openrobotics.org> - 5.0.0-1
- Autogenerated by Bloom

* Tue Mar 21 2023 Tully Foote <tfoote@openrobotics.org> - 4.7.0-3
- Autogenerated by Bloom

