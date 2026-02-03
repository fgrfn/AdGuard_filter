# AdGuard Whitelist

A personal whitelist for AdGuard, Pi-hole, and other DNS-based ad blockers.

## 📋 Description

This repository contains a curated whitelist of domains that should remain accessible despite having an ad blocker active. The list is maintained to ensure that important services and applications function properly.

## 🚀 Usage

### AdGuard

1. Open AdGuard settings
2. Navigate to **Allowlist** (Whitelist)
3. Add the desired domains from `whitelist.txt`

**Or import the list directly:**
```
https://raw.githubusercontent.com/fgrfn/AdGuard_filter/main/whitelist.txt
```

### Pi-hole

1. Open the Pi-hole Admin Interface
2. Navigate to **Whitelist**
3. Add the domains from `whitelist.txt`

**Or import via command line:**
```bash
curl -s https://raw.githubusercontent.com/fgrfn/AdGuard_filter/main/whitelist.txt | sudo tee -a /etc/pihole/whitelist.txt
pihole -w -f /etc/pihole/whitelist.txt
```

## 📦 Included Categories

- **Apple**: iCloud, iTunes, App Store, System Updates
- **GitHub/Microsoft**: GitHub, Copilot, Visual Studio, Azure
- **OpenAI**: ChatGPT, API Services
- **VPN**: Private Internet Access
- **Microsoft Services**: Live, Office 365, Windows Updates
- **CDNs**: Cloudflare, Akamai, Fastly
- **Google Services**: Google APIs, YouTube
- **Development Tools**: Firefox, Docker, npm

## 🔄 Updates

The whitelist is regularly updated when new important domains are identified.

## 📝 Notes

- Using wildcards (`*`) allows whitelisting of subdomains
- Test that the corresponding services work after adding new domains
- Customize the list to fit your personal needs

## 🤝 Contributing

This list is for personal use but feel free to use it as a template.

## 📄 License

Public Domain / Unlicense
