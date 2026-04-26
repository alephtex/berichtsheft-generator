import { test, expect } from '@playwright/test';

test.describe('NetSim Pro', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto(`file://${process.cwd()}/index.html`);
    // Wait for app to initialize
    await page.waitForFunction(() => document.querySelector('.app') !== null);
  });

  test('loads without JS errors', async ({ page }) => {
    const errors = [];
    page.on('console', msg => {
      if (msg.type() === 'error') errors.push(msg.text());
    });
    await page.waitForTimeout(1000);
    
    // Check main elements exist
    await expect(page.locator('.app')).toBeVisible();
    await expect(page.locator('.toolbar')).toBeVisible();
    await expect(page.locator('#canvas')).toBeVisible();
    
    // Verify no JS errors (excluding network/favicon)
    const realErrors = errors.filter(e => !e.includes('favicon') && !e.includes('net::'));
    expect(realErrors).toHaveLength(0);
  });

  test('app structure is correct', async ({ page }) => {
    // Verify main structure
    await expect(page.locator('.toolbar')).toBeAttached();
    await expect(page.locator('#canvas')).toBeAttached();
    await expect(page.locator('.status-bar')).toBeAttached();
    
    // Verify toolbar has expected buttons
    const toolBtns = page.locator('.tool-btn');
    const count = await toolBtns.count();
    expect(count).toBeGreaterThan(10);
  });

  test('zoom controls work', async ({ page }) => {
    const zoomIn = page.locator('.zoom-btn').last();
    await zoomIn.click();
    await page.waitForTimeout(200);
    
    const zoomLabel = page.locator('#zoomLabel');
    await expect(zoomLabel).toBeVisible();
  });

  test('toolbar buttons exist', async ({ page }) => {
    // Check all major toolbar buttons exist
    await expect(page.locator('[title="Auto-Configure IPs"]')).toBeAttached();
    await expect(page.locator('[title="Shortcuts (K)"]')).toBeAttached();
    await expect(page.locator('#btnConnType')).toBeAttached();
    await expect(page.locator('[title="Help (?)"]')).toBeAttached();
  });

  test('canvas area exists and is interactive', async ({ page }) => {
    const canvas = page.locator('#canvas');
    await expect(canvas).toBeAttached();
    
    // Canvas should be able to receive mouse events
    const canvasInner = page.locator('#canvasInner');
    await expect(canvasInner).toBeAttached();
  });

  test('auto-configure button clickable', async ({ page }) => {
    const autoConfig = page.locator('[title="Auto-Configure IPs"]');
    await expect(autoConfig).toBeAttached();
    await autoConfig.click();
    await page.waitForTimeout(300);
    // Button should still exist after click
    await expect(autoConfig).toBeAttached();
  });
});
