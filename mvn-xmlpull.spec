#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-xmlpull
Version  : 1.1.3.1
Release  : 2
URL      : https://repo1.maven.org/maven2/xmlpull/xmlpull/1.1.3.1/xmlpull-1.1.3.1.jar
Source0  : https://repo1.maven.org/maven2/xmlpull/xmlpull/1.1.3.1/xmlpull-1.1.3.1.jar
Source1  : https://repo1.maven.org/maven2/xmlpull/xmlpull/1.1.3.1/xmlpull-1.1.3.1.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Public-Domain
Requires: mvn-xmlpull-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-xmlpull package.
Group: Data

%description data
data components for the mvn-xmlpull package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/xmlpull/xmlpull/1.1.3.1
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/xmlpull/xmlpull/1.1.3.1/xmlpull-1.1.3.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/xmlpull/xmlpull/1.1.3.1
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/xmlpull/xmlpull/1.1.3.1/xmlpull-1.1.3.1.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/xmlpull/xmlpull/1.1.3.1/xmlpull-1.1.3.1.jar
/usr/share/java/.m2/repository/xmlpull/xmlpull/1.1.3.1/xmlpull-1.1.3.1.pom
