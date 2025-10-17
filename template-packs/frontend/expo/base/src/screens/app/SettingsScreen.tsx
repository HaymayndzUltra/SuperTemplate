import React, { useState } from 'react';
import {
  View,
  Text,
  StyleSheet,
  ScrollView,
  TouchableOpacity,
  Switch,
} from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { Ionicons } from '@expo/vector-icons';

export function SettingsScreen() {
  const [notifications, setNotifications] = useState(true);
  const [darkMode, setDarkMode] = useState(false);
  const [biometrics, setBiometrics] = useState(false);
  const [autoSync, setAutoSync] = useState(true);

  const settingsSections = [
    {
      title: 'Preferences',
      items: [
        {
          id: 1,
          title: 'Notifications',
          subtitle: 'Receive push notifications',
          icon: 'notifications-outline',
          type: 'switch',
          value: notifications,
          onValueChange: setNotifications,
        },
        {
          id: 2,
          title: 'Dark Mode',
          subtitle: 'Use dark theme',
          icon: 'moon-outline',
          type: 'switch',
          value: darkMode,
          onValueChange: setDarkMode,
        },
        {
          id: 3,
          title: 'Language',
          subtitle: 'English',
          icon: 'language-outline',
          type: 'nav',
        },
      ],
    },
    {
      title: 'Security',
      items: [
        {
          id: 4,
          title: 'Biometric Login',
          subtitle: 'Use fingerprint or face ID',
          icon: 'finger-print-outline',
          type: 'switch',
          value: biometrics,
          onValueChange: setBiometrics,
        },
        {
          id: 5,
          title: 'Two-Factor Authentication',
          subtitle: 'Not enabled',
          icon: 'shield-checkmark-outline',
          type: 'nav',
        },
      ],
    },
    {
      title: 'Data & Storage',
      items: [
        {
          id: 6,
          title: 'Auto-sync',
          subtitle: 'Sync data automatically',
          icon: 'sync-outline',
          type: 'switch',
          value: autoSync,
          onValueChange: setAutoSync,
        },
        {
          id: 7,
          title: 'Clear Cache',
          subtitle: '45 MB',
          icon: 'trash-outline',
          type: 'nav',
        },
        {
          id: 8,
          title: 'Download Data',
          subtitle: 'Export your data',
          icon: 'download-outline',
          type: 'nav',
        },
      ],
    },
  ];

  const renderSettingItem = (item: any) => {
    return (
      <TouchableOpacity
        key={item.id}
        style={styles.settingItem}
        disabled={item.type === 'switch'}
      >
        <View style={styles.settingLeft}>
          <View style={styles.iconContainer}>
            <Ionicons name={item.icon} size={24} color="#6366f1" />
          </View>
          <View style={styles.textContainer}>
            <Text style={styles.settingTitle}>{item.title}</Text>
            <Text style={styles.settingSubtitle}>{item.subtitle}</Text>
          </View>
        </View>
        {item.type === 'switch' ? (
          <Switch
            value={item.value}
            onValueChange={item.onValueChange}
            trackColor={{ false: '#e5e7eb', true: '#6366f1' }}
            thumbColor={item.value ? '#fff' : '#f3f4f6'}
          />
        ) : (
          <Ionicons name="chevron-forward" size={20} color="#9ca3af" />
        )}
      </TouchableOpacity>
    );
  };

  return (
    <SafeAreaView style={styles.container}>
      <ScrollView contentContainerStyle={styles.scrollContent}>
        <View style={styles.header}>
          <Text style={styles.title}>Settings</Text>
        </View>

        {settingsSections.map((section, index) => (
          <View key={index} style={styles.section}>
            <Text style={styles.sectionTitle}>{section.title}</Text>
            <View style={styles.sectionContent}>
              {section.items.map(renderSettingItem)}
            </View>
          </View>
        ))}

        {/* Footer */}
        <View style={styles.footer}>
          <TouchableOpacity style={styles.footerItem}>
            <Text style={styles.footerText}>Terms of Service</Text>
          </TouchableOpacity>
          <TouchableOpacity style={styles.footerItem}>
            <Text style={styles.footerText}>Privacy Policy</Text>
          </TouchableOpacity>
        </View>
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f9fafb',
  },
  scrollContent: {
    paddingBottom: 24,
  },
  header: {
    paddingHorizontal: 24,
    paddingTop: 16,
    paddingBottom: 24,
  },
  title: {
    fontSize: 28,
    fontFamily: 'Inter-Bold',
    color: '#111827',
  },
  section: {
    marginBottom: 32,
  },
  sectionTitle: {
    fontSize: 14,
    fontFamily: 'Inter-Medium',
    color: '#6b7280',
    textTransform: 'uppercase',
    marginBottom: 8,
    paddingHorizontal: 24,
  },
  sectionContent: {
    backgroundColor: '#fff',
    marginHorizontal: 24,
    borderRadius: 12,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 1 },
    shadowOpacity: 0.05,
    shadowRadius: 2,
    elevation: 2,
  },
  settingItem: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    paddingVertical: 16,
    paddingHorizontal: 20,
    borderBottomWidth: 1,
    borderBottomColor: '#f3f4f6',
  },
  settingLeft: {
    flexDirection: 'row',
    alignItems: 'center',
    flex: 1,
  },
  iconContainer: {
    width: 40,
    height: 40,
    borderRadius: 10,
    backgroundColor: '#6366f110',
    justifyContent: 'center',
    alignItems: 'center',
    marginRight: 16,
  },
  textContainer: {
    flex: 1,
  },
  settingTitle: {
    fontSize: 16,
    fontFamily: 'Inter-Medium',
    color: '#111827',
    marginBottom: 2,
  },
  settingSubtitle: {
    fontSize: 14,
    fontFamily: 'Inter-Regular',
    color: '#6b7280',
  },
  footer: {
    flexDirection: 'row',
    justifyContent: 'center',
    paddingHorizontal: 24,
    paddingTop: 16,
  },
  footerItem: {
    marginHorizontal: 12,
  },
  footerText: {
    fontSize: 14,
    fontFamily: 'Inter-Regular',
    color: '#6366f1',
  },
});